<template>
  <div
    class="card multisteps-form__panel p-3 border-radius-xl bg-white"
    data-animation="FadeIn"
  >
    <h5 class="font-weight-bolder mb-0">About me</h5>
    <p class="mb-0 text-sm">Mandatory informations</p>
    <div class="multisteps-form__content">
      <div class="row mt-3">
        <div class="col-12 col-sm-6">
          <label>First Name</label>
          <soft-input
            id="firstName"
            class="multisteps-form__input"
            type="text"
            placeholder="eg. Michael"
          />
        </div>
        <div class="col-12 col-sm-6 mt-3 mt-sm-0">
          <label>Last Name</label>
          <soft-input
            id="lastName"
            class="multisteps-form__input"
            type="text"
            placeholder="eg. Prior"
          />
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-12 col-sm-6">
          <label>Company</label>
          <soft-input
            id="company"
            class="multisteps-form__input"
            type="text"
            placeholder="eg. Creative Tim"
          />
        </div>
        <div class="col-12 col-sm-6 mt-3 mt-sm-0">
          <label>Email Address</label>
          <soft-input
            id="companyEmail"
            class="multisteps-form__input"
            type="email"
            placeholder="eg. soft@dashboard.com"
          />
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-12 col-sm-6">
          <label>Password</label>
          <soft-input
            id="password"
            class="multisteps-form__input"
            type="password"
            placeholder="******"
          />
        </div>
        <div class="col-12 col-sm-6 mt-3 mt-sm-0">
          <label>Repeat Password</label>
          <soft-input
            id="confirmPassword"
            class="multisteps-form__input"
            type="password"
            placeholder="******"
          />
        </div>
      </div>
      <div class="button-row d-flex mt-4">
        <soft-button
          type="button"
          color="dark"
          variant="gradient"
          class="ms-auto mb-0 js-btn-next"
          @click="this.$parent.nextStep"
          >Next</soft-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import SoftInput from "@/components/SoftInput.vue";
import SoftButton from "@/components/SoftButton.vue";

export default {
  name: "UserInfo",
  components: {
    SoftInput,
    SoftButton,
  },
};
</script>
