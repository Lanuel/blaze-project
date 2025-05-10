
// Thumbnail click handler
document.addEventListener("DOMContentLoaded", function () {
    const thumbnails = document.querySelectorAll(".context-thumb img");
    const mainPhoto = document.querySelector(".main-photo");

    thumbnails.forEach((thumb) => {
        thumb.addEventListener("click", function (e) {
            e.preventDefault();
            // Update main photo src
            mainPhoto.src = this.src;

            // Update thumbnail highlight
            document.querySelectorAll(".context-thumb").forEach(el => el.classList.remove("currentImage"));
            this.closest(".context-thumb").classList.add("currentImage");
        });
    });
});