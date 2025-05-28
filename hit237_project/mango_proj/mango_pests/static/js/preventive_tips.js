document.addEventListener("DOMContentLoaded", () => {
  const resetBtn = document.getElementById("resetChecklist");
  const checklistItems = document.querySelectorAll("#checklist input[type='checkbox']");

  resetBtn.addEventListener("click", () => {
    checklistItems.forEach(item => {
      item.checked = false;
    });
  });
});
