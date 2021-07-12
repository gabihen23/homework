package pageobjects;

import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.PageFactory;

public class BasePage {
	WebDriver driver;

	public BasePage(WebDriver driver) {
		this.driver = driver;
		PageFactory.initElements(driver, this);

	}

	public void fillText(WebElement el, String text) {
		clear(el);
		el.sendKeys(text);
		sleep(1000);
	}

	public void click(WebElement el) {
		el.click();
		sleep(1000);
	}

	public void clear(WebElement el) {
		el.clear();
		sleep(1000);
	}

	public void sleep(int mills) {
		try {
			Thread.sleep(mills);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}

	public String getText(WebElement el) {
		return el.getText();
	}

	public void submit(WebElement el) {
		el.submit();
	}


	public void alertOK() {
		driver.switchTo().alert().accept();
	}

	public void alertOK(String text) {
		driver.switchTo().alert().sendKeys(text);
		driver.switchTo().alert().accept();
	}

	public void moveToElement(WebElement el) {
		Actions action = new Actions(driver);
		action.moveToElement(el).build().perform();
	}
	
	public void scrollToElemnt(WebElement el) {
        JavascriptExecutor js = (JavascriptExecutor) driver;
        js.executeScript("arguments[0].scrollIntoView();", el);
        sleep(500);
	}
	
	public void scrollByPixel(int pixel) {
        JavascriptExecutor js = (JavascriptExecutor) driver;
        js.executeScript("window.scrollBy(0," + pixel + ")");
	}
	
}
