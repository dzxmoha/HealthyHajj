package com.example.zekri.hajjhackaton;

/**
 * Created by zekri on 01/08/2018.
 */

public class Hajj {
    private int id;
    private String name;
    private  String boldtype;
    private int age;

    public String getBoldtype() {
        return boldtype;
    }

    public void setBoldtype(String boldtype) {
        this.boldtype = boldtype;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public Hajj() {

    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
