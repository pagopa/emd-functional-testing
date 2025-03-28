@message
Feature: Send a notification

    Scenario: Onboard user not already onboarded
        Given CitizenA already onboarded on TppFakeEntityIdA
        And a message for the CitizenA
        When a notification request arrives
        Then the response status must be 200
        And the answer must be OK

