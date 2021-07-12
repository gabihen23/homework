package tests;

import static org.testng.Assert.assertEquals;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import pageobjects.TopMenuHeader;

public class changeLanguageTest extends BaseTest {

	@Test(description = "change site language to ES")
	public void TC01_changeSiteLang() {
		TopMenuHeader tmh = new TopMenuHeader(driver);
		tmh.changeLanguage("ES");
		tmh.sleep(3000);
		String siteLang = driver.findElement(By.tagName("html")).getAttribute("lang");
		assertEquals(siteLang, "es-ES");
	}

}
