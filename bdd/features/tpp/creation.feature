@tpp
Feature: Onboard a tpp

    Scenario: Onboard tpp not onboarded
        Given tppD not onboarded
        When an onboarding for TppD request arrives
        Then the onboarding request is successful

    Scenario: Onboard tpp already onboarded
        Given tppA already onboarded
        When an onboarding for TppA request arrives
        Then the onboarding request fail


