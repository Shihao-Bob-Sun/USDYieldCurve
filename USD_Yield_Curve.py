
from math import log, exp
import datetime
import calendar
from dateutil.relativedelta import relativedelta


class USDYieldCurve:

    def __init__(self, depoRates_file, futuresPrices_file, tradeDate_file, holidayCalendar_file):
        # self.holidays
        self.holidays = open("./"+holidayCalendar_file, "r")
        
        # Transform self.holidays:
        # converting self.holidays into a dictionary with keys being dates and values being futures prices
        
        holiday_list = self.holidays.read().splitlines()
        holidays = []
        for i in range(0,len(holiday_list)):
            day = holiday_list[i]
            day = datetime.date(*(int(s) for s in day.split('-')))
            holidays.append(day)
        self.holidays = holidays
        
        
        # self.spotDate
        tradeDate_file = open("./"+tradeDate_file, "r")
        tradeDate = tradeDate_file.read()
        
        self.spotDate = datetime.date(*(int(s) for s in tradeDate.split('-')))
        self.spotDate = self.spotDate + datetime.timedelta(2)
        while self.spotDate.weekday() == 5 or self.spotDate.weekday() == 6 or (self.spotDate in self.holidays):
            self.spotDate = self.spotDate + datetime.timedelta(1)
        self.spotDate = self.spotDate.strftime('%Y-%m-%d')
        
        
        # self.depoRates
        self.depoRates = open("./"+depoRates_file, "r")
        
        # Transform self.depoRate: 
        # converting self.depoRates into a dictionary with keys being dates and values being deposit rates
        depoRate_dic = {}
        spotDate = datetime.date(*(int(s) for s in self.spotDate.split('-')))
        for line in self.depoRates: 
            num=int(line[3])
            
            if line[4]=='D':
                Date = spotDate + datetime.timedelta(num)
            if line[4]=='W':
                Date = spotDate + datetime.timedelta(weeks=num)
            if line[4]=='M':
                Date = spotDate + relativedelta(months=num)
            depoRate_dic[Date]=line.split()[1]
        self.depoRates = depoRate_dic
        
        
        # self.futuresPrices
        self.futuresPrices = open("./"+futuresPrices_file, "r")
        
        # Transform self.futuresPrice:
        # converting self.futuresPrice into a dictionary with keys being dates and values being futures prices
        futuresPrices_dic = {}
        c = calendar.Calendar(firstweekday=calendar.SUNDAY)

        for line in self.futuresPrices: 
            if line[:3]=='EDH':
                month=3
                if int(line[3])>=int(tradeDate[3]):
                    year=int(tradeDate[:3])*10+int(line[3])
                elif int(line[3])==int(tradeDate[3]) and month>int(tradeDate[5:7]):
                    year=int(tradeDate[:3])*10+int(line[3])
                elif int(line[3])==int(tradeDate[3]) and month==int(tradeDate_str[5:7]):
                    year=int(tradeDate[:3])*10+int(line[3])
                    monthcal = c.monthdatescalendar(year,month)
                    if [day for week in monthcal for day in week if \
                        day.weekday() == calendar.WEDNESDAY and \
                        day.month == month][2].strftime('%d')>int(tradeDate[8:10]):
                        year=int(tradeDate[:3])*10+int(line[3])
                    else:
                        year=int(tradeDate[:3])*10+int(line[3])+10
                else:
                    year=int(tradeDate[:3])*10+int(line[3])+10
                monthcal = c.monthdatescalendar(year,month)
                thirdWednesday_date = [day for week in monthcal for day in week if \
                                       day.weekday() == calendar.WEDNESDAY and day.month == month][2]
                futuresPrices_dic[thirdWednesday_date]=line.split()[1]
            if line[:3]=='EDM':
                month=6
                if int(line[3])>=int(tradeDate[3]):
                    year=int(tradeDate[:3])*10+int(line[3])
                elif int(line[3])==int(tradeDate[3]) and month>int(tradeDate[5:7]):
                    year=int(tradeDate[:3])*10+int(line[3])
                elif int(line[3])==int(tradeDate[3]) and month==int(tradeDate[5:7]):
                    year=int(tradeDate[:3])*10+int(line[3])
                    monthcal = c.monthdatescalendar(year,month)
                    if [day for week in monthcal for day in week if \
                        day.weekday() == calendar.WEDNESDAY and day.month == month][2].strftime('%d')>int(tradeDate[8:10]):
                        year=int(tradeDate[:3])*10+int(line[3])
                    else:
                        year=int(tradeDate[:3])*10+int(line[3])+10
                else:
                    year=int(tradeDate[:3])*10+int(line[3])+10
                monthcal = c.monthdatescalendar(year,month)
                thirdWednesday_date = [day for week in monthcal for day in week if \
                                       day.weekday() == calendar.WEDNESDAY and day.month == month][2]
                futuresPrices_dic[thirdWednesday_date]=line.split()[1]
            if line[:3]=='EDU':
                month=9
                if int(line[3])>=int(tradeDate[3]):
                    year=int(tradeDate[:3])*10+int(line[3])
                elif int(line[3])==int(tradeDate[3]) and month>int(tradeDate[5:7]):
                    year=int(tradeDate[:3])*10+int(line[3])
                elif int(line[3])==int(tradeDate[3]) and month==int(tradeDate[5:7]):
                    year=int(tradeDate[:3])*10+int(line[3])
                    monthcal = c.monthdatescalendar(year,month)
                    if [day for week in monthcal for day in week if day.weekday() == calendar.WEDNESDAY and \
                        day.month == month][2].strftime('%d')>int(tradeDate[8:10]):
                        year=int(tradeDate[:3])*10+int(line[3])
                    else:
                        year=int(tradeDate[:3])*10+int(line[3])+10
                else:
                    year=int(tradeDate[:3])*10+int(line[3])+10
                monthcal = c.monthdatescalendar(year,month)
                thirdWednesday_date = [day for week in monthcal for day in week if day.weekday() == calendar.WEDNESDAY and \
                                       day.month == month][2]
                futuresPrices_dic[thirdWednesday_date]=line.split()[1]
            if line[:3]=='EDZ':
                month=12
                if int(line[3])>=int(tradeDate[3]):
                    year=int(tradeDate[:3])*10+int(line[3])
                elif int(line[3])==int(tradeDate[3]) and month>int(tradeDate[5:7]):
                    year=int(tradeDate[:3])*10+int(line[3])
                elif int(line[3])==int(tradeDate[3]) and month==int(tradeDate[5:7]):
                    year=int(tradeDate[:3])*10+int(line[3])
                    monthcal = c.monthdatescalendar(year,month)
                    if [day for week in monthcal for day in week if day.weekday() == calendar.WEDNESDAY and \
                        day.month == month][2].strftime('%d')>int(tradeDate[8:10]):
                        year=int(tradeDate[:3])*10+int(line[3])
                    else:
                        year=int(tradeDate[:3])*10+int(line[3])+10
                else:
                    year=int(tradeDate[:3])*10+int(line[3])+10
                monthcal = c.monthdatescalendar(year,month)
                thirdWednesday_date = [day for week in monthcal for day in week if day.weekday() == calendar.WEDNESDAY and \
                                       day.month == month][2]
                futuresPrices_dic[thirdWednesday_date]=line.split()[1]
        self.futuresPrices = futuresPrices_dic
        
        
        self.DfTable = {}
        
    
    def isHolidayOrWeekends(self,date):
        for i in self.holidays:
            if date == i:
                return True
            if date.weekday()==5 or date.weekday()==6:
                return True
        return False
    

    def dayAdjustment(self,date):
        currentDate = date
        currentMonth = date.month

        while True:
            if self.isHolidayOrWeekends(date):
                date = date+datetime.timedelta(1)
            else:
                return date

            while self.isHolidayOrWeekends(date):
                date = date+datetime.timedelta(1)

            break

        if currentMonth != date.month:
            date = date-datetime.timedelta(1)
        else:
            return date

        while True:
            if self.isHolidayOrWeekends(date):
                date = date-datetime.timedelta(1)
            else:
                return date
            while self.isHolidayOrWeekends(date):
                date = date-datetime.timedelta(1)
            break

        return date
    
    
    def DF(self, d1, d2, R):
        df = (1+R*(d2-d1).days/360)**(-1)
        return df
    
    
    def depoRates2DfTable(self):
        
        # perform date adjustment for dates in depoRate dictionary
        depoRates_adjusted = {}
        for key in self.depoRates:
            key_adjusted = self.dayAdjustment(key)
            depoRates_adjusted[key_adjusted] = self.depoRates[key] 
        self.depoRates = depoRates_adjusted
        
        # calculating discount factor
        spot = datetime.date(*(int(s) for s in self.spotDate.split('-')))
        for i in self.depoRates:
            self.depoRates[i] = self.DF( spot, i, float(self.depoRates[i])/100 )
    
    
    def impliedRate(self,future_price):
        R = (100.0-future_price)/100.0
        return R
    
    
    def futuresPrices2Rates(self):
        # perform date adjustment for dates in futuresPrices dictionary
        futuresPrices_adjusted = {}
        for key in self.futuresPrices:
            key_adjusted = self.dayAdjustment(key)
            futuresPrices_adjusted[key_adjusted] = self.futuresPrices[key]
        self.futuresPrices = futuresPrices_adjusted

        # calculating implied rates from futures prices
        for i in self.futuresPrices:
            self.futuresPrices[i] = self.impliedRate(float(self.futuresPrices[i]))
    
    
    def LogInterpolation(self, d, d1, d2, df1, df2):
        Log_df = log(df1) + ((d-d1).days/(d2-d1).days)*(log(df2)-log(df1))
        return exp(Log_df)
    
    
    def futuresPrices2DfTable(self):
        # finding last two dates in self.depoRates
        depoKeys = list(self.depoRates.keys())
        depoDate_last = depoKeys[-1]
        depoDate_2_last = depoKeys[ depoKeys.index(depoDate_last)-1 ]
        
        df_futures = {}
        
        # finding df_s month
        df_s_month = list(self.futuresPrices.keys())[0]
        
        if df_s_month > list(self.depoRates.keys())[-1]:
            raise Exception("Insufficient LIBOR cash rate data")
        
        for i in self.futuresPrices:
            if df_s_month<i<depoDate_last:
                df_s_month = i

        # calculating df_s
        df_futures[df_s_month] = self.LogInterpolation(df_s_month, 
                                                       depoDate_2_last, 
                                                       depoDate_last, 
                                                       self.depoRates[depoDate_2_last], 
                                                       self.depoRates[depoDate_last])
        
        # transforming futures prices dictionary to a dictionary with values being discount factors
        futuresKeys=list(self.futuresPrices.keys())
        index=futuresKeys.index(df_s_month)
        for i in range(index+1,len(futuresKeys)):
            df_futures[futuresKeys[i]] = df_futures[futuresKeys[i-1]]*self.DF(futuresKeys[i-1],
                                                                              futuresKeys[i],
                                                                              self.futuresPrices[futuresKeys[i-1]])
        
        self.futuresPrices = df_futures
    
    
    def getDfTable(self):
        DfTable_unsorded = {**self.depoRates, **self.futuresPrices}
        DfTable = {}
        
        sortedKeys = sorted(DfTable_unsorded)
        for key in sortedKeys:
            DfTable[key] = DfTable_unsorded[key]
        self.DfTable = DfTable
    
    
    def getNearestTwoDates(self, date):
        date1 = list(self.DfTable.keys())[0]
        date2 = list(self.DfTable.keys())[0]
    
        for day in self.DfTable:
            if day <= date:
                date1 = day
            if day > date:
                date2 = day
                break
    
        return date1, date2
    
    
    def getDfToDate(self, date):
        
        if self.DfTable == {}:
            self.depoRates2DfTable()
            self.futuresPrices2Rates()
            self.futuresPrices2DfTable()
            self.getDfTable()
        
        date = datetime.date(*(int(s) for s in date.split('-')))
        spotDate = datetime.date(*(int(s) for s in self.spotDate.split('-')))
        
        if (date < list(self.DfTable.keys())[0]):
            date1 = spotDate
            date2 = list(self.DfTable.keys())[0]
            df = self.LogInterpolation(date, date1, date2, 1, self.DfTable[date2])
            return df
    
        if date < spotDate or date > list(self.DfTable.keys())[-1] or date > spotDate+relativedelta(years=3):
            raise Exception('Date entered is invalid. Cannot build the curve from given input.')
        else:
            date1, date2 = self.getNearestTwoDates(date)
            df = self.LogInterpolation(date, date1, date2, self.DfTable[date1], self.DfTable[date2])
            return df
    
    
    def getFwdRate(self, date1, date2):
        d1 = datetime.date(*(int(s) for s in date1.split('-')))
        d2 = datetime.date(*(int(s) for s in date2.split('-')))
        spotDate = datetime.date(*(int(s) for s in self.spotDate.split('-')))
        
        if self.DfTable == {}:
            self.depoRates2DfTable()
            self.futuresPrices2Rates()
            self.futuresPrices2DfTable()
            self.getDfTable()
    
        if d1 < spotDate or d1>=d2 or d2 > list(self.DfTable.keys())[-1] or d2 > spotDate+relativedelta(years=3):
            raise Exception('Date entered is invalid. Cannot build the curve from given input.')
        else:
            FwdRate = (360/(d2-d1).days) * (self.getDfToDate(date1)/self.getDfToDate(date2) - 1)
            return FwdRate

