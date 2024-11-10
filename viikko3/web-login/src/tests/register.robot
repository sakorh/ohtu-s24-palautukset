*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle2
    Set Password  kalle222
    Set Password Confirmation    kalle222
    Submit New Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle234
    Set Password Confirmation  kalle234
    Submit New Credentials
    Registration Should Fail With Message  Username should be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  kalle2
    Set Password  kall3
    Set Password Confirmation  kall3
    Submit New Credentials
    Registration Should Fail With Message  Password should contain at least 8 characters and they should not all be alphabetic
    

Register With Valid Username And Invalid Password
    Set Username  kalle2
    Set Password  salasana
    Set Password Confirmation  salasana
    Submit New Credentials
    Registration Should Fail With Message  Password should contain at least 8 characters and they should not all be alphabetic

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle2
    Set Password  kalle123
    Set Password Confirmation  kalle234
    Submit New Credentials
    Registration Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit New Credentials
    Registration Should Fail With Message  Username already in use

Login After Successful Registration
    Set Username  kalle2
    Set Password  kalle222
    Set Password Confirmation    kalle222
    Submit New Credentials
    Registration Should Succeed
    Click Link  ohtu
    Click Button  Logout
    Go To Login Page
    Set Username  kalle2
    Set Password  kalle222
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  kalle2
    Set Password  kall3
    Set Password Confirmation  kall3
    Submit New Credentials
    Registration Should Fail With Message  Password should contain at least 8 characters and they should not all be alphabetic
    Click Link  Login
    Set Username  kalle2
    Set Password  kalle3
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit New Credentials
    Click Button  Register

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}


Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page