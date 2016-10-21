__author__ = 'Sam C'
from array import array
from datetime import  datetime

class Calendar:
    cellContext = ''
    LabelDays = array("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
    currYear = 0
    currMonth = 0
    currDay = 0
    currDate = None
    daysInMonth = 0
    sundayBegining= True
    navHref = None

    def __init__(self):
        # for referesh the page
        Event.addEvent(self)

    #show the calendar
    def displayCal(self,month = None, year = None, attributes = False):
        if(None == year && len(request.Get['year']) > 0):
            year = request.Get['year']
        elif (None == year):
            year = datetime.now("%Y")
            return None

            if(None == month && len(request.Get['month'])> 0 ):
                month = request.Get['month']
            elif (None == month):
                month = datetime.now("%m")

            Calendar.currYear = year
            Calendar.currMonth = month
            Calendar.daysinMonth = Calendar.daysInMonth(month, year)

            # context = '<div id="calendar">'
            #                               '<div class="box">'
            #                               +createNavi()
            #                               + '</div>'
            #                               + '<div class="box-content">'
            #                               + '<ul class="label">'+creatLabel()+'</ul>'
            #                               context+='<div class="clear"></div>'
            #                                 context+='<ul class="dates">'
            #                                 for i in xrange(weeksInMonth(month,year)):
            #                                     for j in range(1,7):
            #                                         context+= showDay(i*7+j,attributes)
            #
            #                               context+='</ul>'
            #                               context+='<div class="clear"></div>'
            #           context+='</div>'
            #       context+='</div>'
            return None

            #ul and li element creation
    def displayDay(self, cellNum, attrib = False):
        if (Calendar.currDay == 0):
            # to start from Sunday we put 1 and 2 sart the day with monday
            beginningDayOfTheWeek = datetime.strptime(Calendar.currYear+'-'+Calendar.currMonth+'-01')
            if(Calendar.sundayBegining):
                if(beginningDayOfTheWeek == 7):
                    beginningDayOfTheWeek = 1
                else:
                    beginningDayOfTheWeek+1

            if(int(cellNum) == int(beginningDayOfTheWeek)):
                Calendar.currDay = 1

            if((Calendar.currDay != 0)&&(Calendar.currDay <= Calendar.daysInMonth)):
                Calendar.currDate = datetime.strptime(Calendar.currYear+'-'+Calendar.currMonth+'-'+Calendar.currMonth, 'Y-m-d')
                Calendar.cellContext = Calendar.provideCellContext(attrib)
                Calendar.currDay+1
            else:
                Calendar.currDate = None
                cellNum = None

        return  '<li id="li-'+Calendar.currDate+'" class="'(cellNum%7==1 and ' start ' or (cellNum%7==0 and ' end ' or ' '))\
                + (Calendar.cellContext== None and 'mask' or '')+'">'+Calendar.cellContext+'</li>'


    # create navigation for prev and next
    def createNavi(self):
        return None

    # come up with number of weeks in a month
    def weeksInMonth(self):
        return None

    def daysInMonth(self):
        return None

    def createLabel(self):
        return None

    def setSunday(bool = True):
        Calendar.sundayBegining = bool

    def getCurrentDate(self):
        return Calendar.currentDate

        # I can pull any event for specific day
    def provideCellContext(setup = False):
        Calendar.cellContent = None
        Calendar.cellContent = Calendar.currentDate + Event.EventName()
        return Calendar.cellContent

    def searchCal(self):
        return None


class Event:
    def __init__(self, date, description ):
        self.__names = []
        self.__date = date
        self.__description = description

        self._cellContent  = []

    def EventName(self):
        return self.__name

    def EventDate(self):
        return self.__date

    def EventDescription(self):
        return self.__description

    def addEvent(self, Calender):
        self.__names.append(Calendar)





