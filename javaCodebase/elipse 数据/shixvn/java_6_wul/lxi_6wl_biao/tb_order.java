package lxi_6wl_biao;

public class tb_order {
	private int id;
	
	private String name;
	private String orderid;
	private String descinfo;
	
	private double price;

	public tb_order(int id, String name, String orderid, String descinfo, double price) {
		super();
		this.id = id;
		this.name = name;
		this.orderid = orderid;
		this.descinfo = descinfo;
		this.price = price;
	}

	@Override
	public String toString() {
		return "tb_order [id=" + id + ", name=" + name + ", orderid=" + orderid + ", descinfo=" + descinfo + ", price="
				+ price + "]";
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

	public String getOrderid() {
		return orderid;
	}

	public void setOrderid(String orderid) {
		this.orderid = orderid;
	}

	public String getDescinfo() {
		return descinfo;
	}

	public void setDescinfo(String descinfo) {
		this.descinfo = descinfo;
	}

	public double getPrice() {
		return price;
	}

	public void setPrice(double price) {
		this.price = price;
	}
	
	
	
	
}
