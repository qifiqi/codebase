package driverSocker


//Serializable 表示进行序列化,序列化的对象才可以通过socket进行传递
class Task extends Serializable {
  //  要发送的数据

  val datas = List(1, 2, 3, 4, 5)
  //定义的算法
  val login = (num: Int) => num * 2

  //  定义计算函数
  def compute(): List[Int] = {
    datas.map(login)
  }


}
