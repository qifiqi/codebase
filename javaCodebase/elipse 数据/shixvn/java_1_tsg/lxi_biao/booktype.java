package lxi_biao;

public class booktype {
	private int typeid;
	private String typename;

	public booktype(int typeid, String typename) {
		super();
		this.typeid = typeid;
		this.typename = typename;
	}

	@Override
	public String toString() {
		return "booktype [typeid=" + typeid + ", typename=" + typename + "]";
	}

	public int getTypeid() {
		return typeid;
	}

	public void setTypeid(int typeid) {
		this.typeid = typeid;
	}

	public String getTypename() {
		return typename;
	}

	public void setTypename(String typename) {
		this.typename = typename;
	}

}
