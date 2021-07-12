package tests;

import static org.testng.Assert.assertEquals;

import org.testng.annotations.Test;

import pageobjects.TopMenuHeader;

public class checkMenuButtonsTest extends BaseTest {

	@Test(description = "check menu options")
	public void TC01_checkMenuOptions() {
		TopMenuHeader tmh = new TopMenuHeader(driver);
		assertEquals(tmh.checkMenuOptions(), true);
	}

}
