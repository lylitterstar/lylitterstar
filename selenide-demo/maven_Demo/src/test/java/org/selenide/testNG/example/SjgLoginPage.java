package org.selenide.testNG.example;
import org.testng.annotations.*;
import org.testng.Assert;

import org.openqa.selenium.By;

import static com.codeborne.selenide.Selenide.*;

/**
 * Created by dushanshan on 17-9-18.
 */
public class SjgLoginPage {
    String url;
    String username;
    String password;
    String title_sign;
    String title_home;
//    @BeforeClass
//    public void beforeClass() {
//        System.out.println("this is before class");
//    }
    @BeforeTest
    public void setUp(){
        url="https://shujuguan.shujuguan.cn/login";
        username="dushanshan@gbase.cn";
        password="123456";
        title_sign="登录-数据观";
        title_home="数据观 - 所有人都能使用的数据分析工具";
    }
    @DataProvider(name="user")
    public  Object[][]Users(){
        return new Object[][]{
                {"dushanshan@gbase.cn","123456"},
        };
    }
    @Test(groups = "sjg", dataProvider="user")
    public void testLogin(String user,String pwd) {
        open(url);
        Assert.assertEquals(title(),title_sign);
        $(By.id("username")).sendKeys(user);
        $(By.name("password")).sendKeys(pwd);
        $(By.className("btn-submit")).click();
        sleep(5);
        forward();
        System.out.println("test title:" + title());
        Assert.assertEquals(title(),title_home);
        screenshot("testLogin.png");

    }
    @Test(groups = "sjg")
    public void testSJGPrint1(){
        System.out.println("sjgClass test method 1");
    }

    @Test(groups = "sjg")
    public void testSJGPrint2(){
        System.out.println("sjgClass test method 2");
    }
    @AfterTest
    public void afterClass(){
        System.out.println("this is after class");
    }

}
