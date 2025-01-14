@tpp
Feature: Change tpp state
    
    Scenario: Tpp tpp not onboarded
        Given tppA never onboarded
        When a state change for TppA request arrives
        Then the state change request fail

    Scenario: Tpp already onboarded
        Given tppA already onboarded
        When a state change for TppA request arrives
        Then the state change request is successful


