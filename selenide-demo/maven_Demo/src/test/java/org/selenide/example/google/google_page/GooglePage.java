package org.selenide.example.google.google_page;

import com.codeborne.selenide.Condition;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static com.codeborne.selenide.Selenide.open;
import static com.codeborne.selenide.Selenide.$;
import org.openqa.selenium.By;

/**
 * Created by dushanshan on 17-9-18.
 */

public class GooglePage {

    @Before
    public void  setUp(){

    }
    @Test
    public void testUserSearch(){
        open("https://www.baidu.com/");
        $(By.id("su")).shouldHave(Condition.exactValue("百度一下"));
    }
    @Test
    public void testPrint1(){
        System.out.println("googleClass test method 2");
    }

    @After
    public void teardown(){

    }

}
