@payment
Feature: Send a notification

    Scenario: The user makes a payment attempt for a valid tpp and agent
        Given the user decide to make a payment for TPP TppNameA and has chosen an agent AgentA
        When the user sends a payment request with the entity id EntityIdA and selected an agent AgentA and origin OriginIdA
        Then if the tpp is valid, the system will returns a 200 OK
        And if the agent is valid, the system will returns a 200 OK
        And if both checks pass, the system creates a "Payment Attempt"
        Then the user with fiscal code FiscalCodeA and notice number NoticeNumberA is redirected to the destination link

    Scenario: The user makes a payment attempt for a not valid tpp
        Given the user decide to make a payment for TPP TppNameB and has chosen an agent AgentB
        When the user sends a payment request with the entity id EntityIdB and selected an agent AgentB and origin OriginIdB
        Then if the tpp is not valid, the system will returns a 404

    Scenario: The user makes a payment attempt for a valid tpp and but not a valid agent
        Given the user decide to make a payment for TPP TppNameA and has chosen an agent AgentC
        When the user sends a payment request with the entity id EntityIdA and selected an agent AgentC and origin OriginIdA
        Then if the tpp is valid, the system will returns a 200 OK
        And if the agent is not valid, the system will returns a 404