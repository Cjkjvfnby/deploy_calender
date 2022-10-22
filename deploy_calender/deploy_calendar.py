from calendar import HTMLCalendar

from deploy_calender.month import Day, Month


class DeployCalendar(HTMLCalendar):
    def __init__(self, deploy_days: set[Day], avoid_days: set[Day]):
        super().__init__()
        self.deploy_days = deploy_days
        self.avoid_days = avoid_days

    def _get_day_class(self, day: Day) -> str:
        if day in self.deploy_days:
            return "deployIt"
        elif day in self.avoid_days:
            return "noWay"
        else:
            return "writeSomeCode"

    def formatday(self, day: int, weekday: int) -> str:
        """
        Return a day as a table cell.
        """
        if day == 0:
            # day outside month
            return f'<td class="{self.cssclass_noday}">&nbsp;</td>'
        else:
            weekday_css = self.cssclasses[weekday]
            day_css = self._get_day_class(Day(day))
            return f'<td class="{weekday_css} {day_css}">{day:d}</td>'

    def get_html(self, month: Month) -> str:
        return self.formatmonth(month.year, month.month)
