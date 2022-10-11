package com.lz

object ScalaList {


  def main(args: Array[String]): Unit = {
    val name_list: List[String] = List("sb", "dsb", "wsnmm")
    val list_all = List(1, 2, 3, 4, 5, "sb", "dsb")
    println(name_list, "\n", list_all)
    println(list_all.toList(5))
    println(name_list.tail)
    println(name_list.isEmpty)
    for (i <- name_list.iterator) {
      println(i)
    }
    println("*" * 188)
    val cc = Nil
    println(cc.isEmpty)
    val bb = List()
    println(bb.isEmpty)

    val mm = 1 :: 2 :: 3 :: 4 :: 5 :: 3 :: 6 :: 7 :: Nil
    println(mm
    )

  }


}
