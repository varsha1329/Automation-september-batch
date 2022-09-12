# Created by Vars-ha at 9/7/2022
Feature: check Clear cache is Visible

  Scenario: check Clear Cache Option Visible after click on Setting Icon
    Given enter valid Email & Password
    When Click on Setting Icon
    Then check Clear Cache Option visible
    And close the browser
  Scenario: Check after clear cache Error msg show
    Given valid Email & Password
    When click on clear cache
    Then check error message