package org.selenide.testNG.example;

import com.codeborne.selenide.Condition;
import org.openqa.selenium.By;

import static com.codeborne.selenide.Selenide.$;
import static com.codeborne.selenide.Selenide.open;
import org.testng.annotations.Test;
/**
 * Created by dushanshan on 17-9-18.
 */
public class GooglePage2 {

    @Test(groups = "google")
    public void testUserSearch(){
        open("https://www.baidu.com/");
        $(By.id("su")).shouldHave(Condition.exactValue("百度一下"));
    }
    @Test(groups = "google")
    public void testPrint1(){
        System.out.println("googleClass test method 2");
    }
    @Test(groups = "google")
    public void testPrint2(){
        System.out.println("googleClass test method 2");
    }
}
