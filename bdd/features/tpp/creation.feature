@tpp
Feature: Onboard a tpp

    Scenario: Onboard tpp not onboarded
        Given TppFakeEntityId not onboarded
        When an onboarding for TppFakeEntityId request arrives
        Then the onboarding request is successful

    Scenario: Update tpp already onboarded
        Given TppFakeEntityId already onboarded
        When an updating for TppFakeEntityId request arrives
        Then the onboarding request is successful

    Scenario: Onboard tpp already onboarded
        Given TppFakeEntityId already onboarded
        When an onboarding for TppFakeEntityId request arrives
        Then the onboarding request fail

    Scenario: Change state to a tpp already onboarded
        Given TppFakeEntityId already onboarded
        When an change state for TppFakeEntityId request arrives
        Then the changing request is successful