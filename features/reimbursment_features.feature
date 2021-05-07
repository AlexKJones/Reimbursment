Feature: Reimbursment Features

  Scenario: Login without id displays undefined
    Given The User is on the Home Page
    When The User clicks on Log In
    Then The Employee fields should display undefined

  Scenario: Login with id Logs in user and displays employee data
    Given The User is on the Home Page
    When The User clicks on login field and then clicks the login button
    Then The User should be logged in and showing data

  Scenario: User tries to view a request that doesnt exist
    Given The User is logged in
    When The User puts bad credentials on request fields and then clicks the view button
    Then The Notification field should read 404 request not found

  Scenario: User tries to view a request that they can view
    Given The User is logged in
    When The User puts in credentials on request fields and then clicks the view button
    Then The Notification field should read 200 succefully found request

  Scenario: User logs out
    When The User clicks the log out button
    Then The Notification field should read Logged Out

  Scenario: Supervisor approves request
    Given The Supervisor is logged in
    When The Supervisor views the request and clicks approve
    Then The Notification field should read Approved by Supervisor awaiting Department Head approval

  Scenario: Department Head approves request
    Given The Department Head is logged in
    When The Department Head views the request and clicks approve
    Then The Notification field should read Approved by DH awaiting approval from BenCo

  Scenario: BenCo approves request
    Given The BenCo is logged in
    When The BenCo views the request and clicks approve
    Then The Notification field should read REQUEST APPROVED

  Scenario: Request is Approved
    Given The BenCo has approved the request
    When The user logs in and views request
    Then The is_approved field should read true

  Scenario: Supervisor Denies the request
    Given The supervisor denies a request
    When The supervisor logs in and views request inserts a 0 reason for denail and clicks deny
    When The user logs in and views request
    Then The is_denied field should read true
