function openUserEditPopup() {
  document.getElementById("userEditPopup").style.display = "flex";
}

function closeUserEditPopup() {
  document.getElementById("userEditPopup").style.display = "none";
}

function openUserEditPopup(button) {
  const userId = button.getAttribute("data-user-id");
  const departmentId = button.getAttribute("data-department-id");
  const adminFlg = button.getAttribute("data-admin-flg") === "true";

  // フォームに値をセット
  document.getElementById("popup-user-id").value = userId;
  document.getElementById("popup-department-select").value = departmentId;
  document.getElementById("popup-admin-true").checked = adminFlg;
  document.getElementById("popup-admin-false").checked = !adminFlg;

  document.getElementById("userEditPopup").style.display = "flex";
}
