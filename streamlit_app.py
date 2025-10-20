import streamlit as st
import pandas as pd

def main():
    st.title("Ứng dụng nhập dữ liệu bằng Streamlit")

    # Chọn phương thức nhập dữ liệu ở sidebar
    option = st.sidebar.radio(
        "Chọn phương thức nhập dữ liệu:",
        ("Nhập thủ công", "Tải tệp (CSV/TXT/Excel)")
    )

    # Nếu người dùng chọn "Nhập thủ công"
    if option == "Nhập thủ công":
        st.subheader("Nhập dữ liệu thủ công")

        # Ví dụ: ta giả sử có 3 cột: 'loan_amount', 'rate_of_interest', 'Gender'
        loan_amount = st.number_input("Nhập loan_amount:", min_value=0.0, step=1000.0)
        rate_of_interest = st.number_input("Nhập rate_of_interest:", min_value=0.0, step=0.1)
        gender = st.selectbox("Chọn Gender:", ["Male", "Female", "Unknown", "Joint"])

        # Khi nhấn nút "Thêm vào DataFrame"
        if st.button("Thêm vào DataFrame"):
            if "manual_data" not in st.session_state:
                st.session_state["manual_data"] = pd.DataFrame(columns=["loan_amount", "rate_of_interest", "Gender"])
            
            new_row = {
                "loan_amount": loan_amount,
                "rate_of_interest": rate_of_interest,
                "Gender": gender
            }
            # Ở phiên bản mới của pandas, append() được khuyến cáo thay thế bằng concat
            st.session_state["manual_data"] = pd.concat(
                [st.session_state["manual_data"], pd.DataFrame([new_row])],
                ignore_index=True
            )
            st.success("Đã thêm dòng dữ liệu thành công!")

        # Hiển thị DataFrame nhập tay (nếu có)
        if "manual_data" in st.session_state and not st.session_state["manual_data"].empty:
            st.write("Dữ liệu đã nhập:")
            st.dataframe(st.session_state["manual_data"])

    # Nếu người dùng chọn "Tải tệp"
    else:
        st.subheader("Tải tệp dữ liệu")
        uploaded_file = st.file_uploader("Chọn tệp CSV, TXT, hoặc Excel", type=["csv", "txt", "xlsx", "xls"])

        if uploaded_file is not None:
            file_details = {
                "filename": uploaded_file.name,
                "filetype": uploaded_file.type,
                "filesize": uploaded_file.size
            }
            st.write(file_details)

            # Đọc dữ liệu từ file
            try:
                if uploaded_file.name.endswith(".csv"):
                    df = pd.read_csv(uploaded_file)
                elif uploaded_file.name.endswith(".txt"):
                    # Giả sử file txt được phân tách bằng dấu phẩy hoặc tab
                    df = pd.read_csv(uploaded_file, sep=None, engine='python')
                elif uploaded_file.name.endswith(".xlsx") or uploaded_file.name.endswith(".xls"):
                    df = pd.read_excel(uploaded_file)
                else:
                    st.error("Định dạng tệp không được hỗ trợ!")
                    return

                st.success("Tải file thành công!")
                st.dataframe(df)

            except Exception as e:
                st.error(f"Lỗi khi đọc file: {e}")

if __name__ == "__main__":
    main()
