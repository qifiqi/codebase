package csgl_biao;

public class tb_goods {
	private int  goodid;
	private int num;

	private String goodname;
	
	private double price;

	public int getGoodid() {
		return goodid;
	}

	public void setGoodid(int goodid) {
		this.goodid = goodid;
	}

	public int getNum() {
		return num;
	}

	public void setNum(int num) {
		this.num = num;
	}

	public String getGoodname() {
		return goodname;
	}

	public void setGoodname(String goodname) {
		this.goodname = goodname;
	}

	public double getPrice() {
		return price;
	}

	public void setPrice(double price) {
		this.price = price;
	}

	@Override
	public String toString() {
		return "tb_goods [goodid=" + goodid + ", num=" + num + ", goodname=" + goodname + ", price=" + price + "]";
	}

	public tb_goods(int goodid, int num, String goodname, double price) {
		super();
		this.goodid = goodid;
		this.num = num;
		this.goodname = goodname;
		this.price = price;
	}

	
}
