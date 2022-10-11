package driverSocker

import java.io.ObjectInputStream
import java.net.{ServerSocket, Socket}

object Driver {


  def main(args: Array[String]): Unit = {
    //    启动服务端,监听8088端口
    val server = new ServerSocket(8088)
    println("ok等待客户端连接")
    //  等待客户端连接
    val client: Socket = server.accept();
    //    获取客户端的输入流
    val in = client.getInputStream
    val objin = new ObjectInputStream(in)
    //    读取输入的数据
    //    val i = in.read()
    //读取输入的对象并转换成对应的实例
    val task = objin.readObject().asInstanceOf[Task]
//对发送过来的进行运算
    val i:List[Int] = task.compute()
    println(i)
    //    关闭
    in.close()
    client.close()
    server.close()

  }

}
