package vacation_biao;


public class inoculatetable {
	private int inoculateid;

	private  String city;
	private  String community;
	private  String name;
	private  String gender;
	private  String type;
	private  String phone;
	private  String id_number;

	private static String time;

	@SuppressWarnings("static-access")
	public inoculatetable(int inoculateid, String city, String community, String name, String gender, String type,
			String phone, String id_number, String time) {
		super();
		this.inoculateid = inoculateid;
		this.city = city;
		this.community = community;
		this.name = name;
		this.gender = gender;
		this.type = type;
		this.phone = phone;
		this.id_number = id_number;
		this.time = time;
	}

	@Override
	public String toString() {
		return "inoculatetable [inoculateid=" + inoculateid + ", city=" + city + ", community=" + community + ", name="
				+ name + ", gender=" + gender + ", type=" + type + ", phone=" + phone + ", id_number=" + id_number
				+ ", time=" + time + "]";
	}

	public int getInoculateid() {
		return inoculateid;
	}

	public void setInoculateid(int inoculateid) {
		this.inoculateid = inoculateid;
	}

	public String getCity() {
		return city;
	}

	public void setCity(String city) {
		this.city = city;
	}

	public String getCommunity() {
		return community;
	}

	public void setCommunity(String community) {
		this.community = community;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getGender() {
		return gender;
	}

	public void setGender(String gender) {
		this.gender = gender;
	}

	public String getType() {
		return type;
	}

	public void setType(String type) {
		this.type = type;
	}

	public String getPhone() {
		return phone;
	}

	public void setPhone(String phone) {
		this.phone = phone;
	}

	public String getId_number() {
		return id_number;
	}

	public void setId_number(String id_number) {
		this.id_number = id_number;
	}

	public static String getTime() {
		return time;
	}

	public static void setTime(String time) {
		inoculatetable.time = time;
	}

}
