@message_core
Feature: Send a notification

    Scenario: User onboarded
        Given a message for the citizenA
        When a notification request arrives
        Then the response status must be 200
        And the answer must be OK

    Scenario: User not onboarded
        Given a message for the citizenB
        When a notification request arrives
        Then the response status must be 202
        And the answer must be NO_CHANNELS_ENABLED