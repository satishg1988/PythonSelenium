class AllLocators():
    # All locators from the Orange HRM login page
    username_textbox = "//input[@id='txtUsername']"
    password_textbox = "//input[@id='txtPassword']"
    login_button = "btnLogin"

    # All locators on the Orange HRM landing page
    welcome_admin_link = "//a[contains(text(), 'Welcome')]"
    logout_link = "//a[contains(text(), 'Logout')]"
    header_leave_link = "//a[@id='menu_leave_viewLeaveModule']"
    header_menu_bar = "//ul[@id='mainMenuFirstLevelUnorderedList']//b"

    # All locators on the Leave-->Leave List page
    fromdate_field = "//input[@id='calFromDate']/following-sibling::img"
    todate_field = "//input[@id='calToDate']/following-sibling::img"
    year_leavelist = "//select[@data-handler='selectYear']//option"
    month_leavelist = "//select[@data-handler='selectMonth']//option"
    day_leavelist = "//div[@id='ui-datepicker-div']//tr//a"
    leave_status = "//div[@class='checkbox_group label_first']//label[contains(text(), 'T')]"