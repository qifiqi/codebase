package driverSocker

import java.io.ObjectOutputStream
import java.net.Socket

object Executor {


  def main(args: Array[String]): Unit = {
    //    创建客户端连接,连接服务器,localhost本地,8088端口
    val client = new Socket("localhost", 8088)
    //    获取输出流
    val out = client.getOutputStream()
    //    创建用来发送数据的流
    val objOut = new ObjectOutputStream(out)
    //    创建发送的task对象
    var task = new Task()

//    发送对象到服务器
    objOut.writeObject(task)
    //    向服务器发送信息
    //    out.write(123)
    //    清空缓存
    out.flush()
    //    关闭流
    out.close()
    println("ok")
  }

}
