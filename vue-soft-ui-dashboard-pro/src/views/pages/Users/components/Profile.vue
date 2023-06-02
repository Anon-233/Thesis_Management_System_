<template>
  <div
    class="card multisteps-form__panel p-3 border-radius-xl bg-white"
    data-animation="FadeIn"
  >
    <h5 class="font-weight-bolder mb-0">Profile</h5>
    <div class="multisteps-form__content mt-3">
      <div class="row">
        <div class="col-12">
          <label>Public Email</label>
          <soft-input
            id="email"
            class="multisteps-form__input"
            type="text"
            placeholder="Use an address you don't use frequently."
          />
        </div>
        <div class="col-12">
          <label>Bio</label>
          <soft-textarea
            id="bio"
            class="multisteps-form__textarea"
            rows="5"
            placeholder="Say a few words about who you are or what you're working on."
          ></soft-textarea>
        </div>
      </div>
      <div class="button-row d-flex mt-4">
        <soft-button
          type="button"
          color="light"
          variant="gradient"
          class="js-btn-prev"
          @click="this.$parent.prevStep"
          >Prev</soft-button
        >
        <soft-button
          type="button"
          color="dark"
          variant="gradient"
          class="ms-auto"
          >Send</soft-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import SoftInput from "@/components/SoftInput.vue";
import SoftButton from "@/components/SoftButton.vue";
import SoftTextarea from "@/components/SoftTextarea.vue";

export default {
  name: "Profile",
  components: {
    SoftInput,
    SoftButton,
    SoftTextarea,
  },
};
</script>
