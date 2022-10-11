package lxi_biao;

public class bookinfo {
	private int bookid;
	private String bookname;
	private String bookauthor;
	private String bookpublish;
	private float bookprice;
	private String booktype;

	public bookinfo(int bookid, String bookname, String bookauthor, String bookpublish, float bookprice,
			String booktype) {
		super();
		this.bookid = bookid;
		this.bookname = bookname;
		this.bookauthor = bookauthor;
		this.bookpublish = bookpublish;
		this.bookprice = bookprice;
		this.booktype = booktype;
	}

	@Override
	public String toString() {
		return "bookinfo [bookid=" + bookid + ", bookname=" + bookname + ", bookauthor=" + bookauthor + ", bookpublish="
				+ bookpublish + ", bookprice=" + bookprice + ", booktype=" + booktype + "]";
	}

	public int getBookid() {
		return bookid;
	}

	public void setBookid(int bookid) {
		this.bookid = bookid;
	}

	public String getBookname() {
		return bookname;
	}

	public void setBookname(String bookname) {
		this.bookname = bookname;
	}

	public String getBookauthor() {
		return bookauthor;
	}

	public void setBookauthor(String bookauthor) {
		this.bookauthor = bookauthor;
	}

	public String getBookpublish() {
		return bookpublish;
	}

	public void setBookpublish(String bookpublish) {
		this.bookpublish = bookpublish;
	}

	public float getBookprice() {
		return bookprice;
	}

	public void setBookprice(float bookprice) {
		this.bookprice = bookprice;
	}

	public String getBooktype() {
		return booktype;
	}

	public void setBooktype(String booktype) {
		this.booktype = booktype;
	}

}
