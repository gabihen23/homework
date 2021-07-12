package pageobjects;

import java.util.ArrayList;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class TopMenuHeader extends BasePage {

	@FindBy(css = ".headerFirstRow_13p737w img")
	private WebElement logoBtn;
	@FindBy(css = "li.li_8cxs15")
	private List<WebElement> menuBtnsList;
	@FindBy(css = "._8cxs15")
	private WebElement moreBtn;
	@FindBy(css = "[type='button']:nth-of-type(2)")
	private WebElement changeLanguageBtn;
	@FindBy(css = "._6ipfbx")
	private List<WebElement> lanuageOptions;
	String menuOptions[] = { "Premier League", "Transfers", "Champions League", "FanVoice", "The Switch", "EFL",
			"La Liga", "Serie A", "More" };

	public TopMenuHeader(WebDriver driver) {
		super(driver);
	}

	/*
	 * This Method Will Switch The Site Language.
	 */
	public void changeLanguage(String lang) {
		click(changeLanguageBtn);
		sleep(2000);
		for (WebElement el : lanuageOptions) {
			if (getText(el).equalsIgnoreCase(lang)) {
				click(el);
				break;
			}
		}
	}

	/*
	 * This Method Will show more menu options by hovering above the button.
	 */
	public void showMoreMenuOptions() {
		moveToElement(moreBtn);
	}

	/* validations */

	/*
	 * This Method Will validate all menu options are displayed
	 */
	public boolean checkMenuOptions() {
		boolean allMenuBtnsDisplayed = true;
		List<String> displayedMenuOptions = new ArrayList<>();
		List<WebElement> menuElements = driver.findElements(By.className("li_8cxs15"));
		menuElements.add(driver.findElement(By.className("_8cxs15")));
		for (WebElement el : menuElements) {
			displayedMenuOptions.add(el.getAttribute("textContent"));
		}

		for (String item : menuOptions) {

			if (displayedMenuOptions.contains(item)) {
				continue;
			} else {
				System.out.println(item + " button is not displayed in headers menu.");
				allMenuBtnsDisplayed = false;
			}
		}
		return allMenuBtnsDisplayed;
	}

}
