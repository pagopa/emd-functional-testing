@tpp
Feature: Onboard a tpp

    Scenario: Onboard tpp not onboarded
        Given tppA never onboarded
        When an onboarding for TppA request arrives
        Then the creation request is successful

    Scenario: Onboard tpp already onboarded
        Given tppA already onboarded
        When an onboarding for TppA request arrives
        Then the creation request fail


