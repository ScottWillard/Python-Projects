from covid import Covid

covid = Covid()


class Corona:

    def getCovidStats(self):
        print(covid.get_total_active_cases())
        print(covid.get_total_deaths())
        print(covid.get_total_recovered())


Corona.getCovidStats(covid)
