# SauceDemo Automation Bot 🛒

An automated End-to-End (E2E) testing script written in Python using Selenium 4. The bot performs a full purchase flow on the SwagLabs (SauceDemo) training website.

## 🚀 Features
* **Selenium 4 Integration:** Uses the latest Service and Options configuration.
* **Robust Locators:** Uses `WebDriverWait` and explicit waits instead of implicit sleeps for stability.
* **Custom Wrapper:** Implements a `drive_find` helper function to adhere to DRY (Don't Repeat Yourself) principles.
* **Dynamic Elements:** Handles dynamic page loading and elements visibility.

## 🛠️ Tech Stack
* Python 3.x
* Selenium WebDriver
* WebDriver Manager (Automatic driver management)

## 📋 Scenarios Covered
1.  Login with standard credentials.
2.  Adding items to the cart (Backpack & T-Shirt).
3.  Navigating to checkout.
4.  Filling out the shipping form.
5.  Finalizing the order and capturing the success message.

## ⚠️ Note
`time.sleep()` functions are included in the code intentionally to allow visual observation of the bot's actions during demonstration. In a production environment, these would be removed.
