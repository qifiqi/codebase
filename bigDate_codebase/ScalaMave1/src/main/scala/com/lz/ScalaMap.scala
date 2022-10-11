package com.lz

import scala.collection.mutable

object ScalaMap {
  def map_lx(): Unit ={
    val map1:Map[String,Int] = Map("sb"->11,"sss"->12)
    println(map1)
    println(map1("sb"))
    println(map1.getOrElse("sb",2))
    println(map1.getOrElse("sbs",2))
    //    不行报错Exception in thread "main" java.util.NoSuchElementException: key not found: sbs
    //    println(map1("sbs"))
    println("x"*88)
    for (i<-map1){
      println(i)
    }
    println("x"*88)
    map1.foreach{
      case (x,y)=>println(x+"->"+y)
    }
    println("x"*88)
    map1.foreach(println)
    println("x"*88)

    for (i<-map1.keys){
      println(i,map1.get(i))
      println(i,map1.get(i).get)
    }
    var num_c = 10
    var num_k = 9
    for (i<-0 to num_c)println("x"*num_k)
  }

  def main(args: Array[String]): Unit = {
    val map1:mutable.Map[String,Int] = mutable.Map()
    map1("sb") = 12
    map1.put("sb1",20)
    println(map1)
    map1.remove("sb")
    println(map1)



  }

}
