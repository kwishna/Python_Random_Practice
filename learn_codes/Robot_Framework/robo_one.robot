*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${URL}          http://google.co.in/
${BROWSER}      Chrome


*** Test Cases ***
MyFirstTestCase
    Log  This Is My First Test Case  level=INFO

My Second Test Case
    Log  This Is My Second Test Case Which Is First Selenium Test Case.
    Open Browser     ${URL}   browser=${BROWSER}
    Set Browser Implicit Wait   10
    Maximize Browser Window
    Go To    http://google.co.in
    Input Text       name=q               Krishna Poultry Agency
    Sleep            2
    Press Keys    name=q    ENTER
 #   Click Button     xpath://div[@class='FPdoLc VlcLAe']//input[@name='btnK']
 #   Click Element    xpath://a[contains(text(),'THANKS')]
    Close Browser
