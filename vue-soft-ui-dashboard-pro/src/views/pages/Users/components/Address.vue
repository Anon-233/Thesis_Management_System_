<template>
  <div
    class="card multisteps-form__panel p-3 border-radius-xl bg-white"
    data-animation="FadeIn"
  >
    <h5 class="font-weight-bolder">Address</h5>
    <div class="multisteps-form__content">
      <div class="row mt-3">
        <div class="col">
          <label>Address 1</label>
          <soft-input
            id="address1"
            class="multisteps-form__input"
            type="text"
            placeholder="eg. Street 111"
          />
        </div>
      </div>
      <div class="row mt-3">
        <div class="col">
          <label>Address 2</label>
          <soft-input
            id="address2"
            class="multisteps-form__input"
            type="text"
            placeholder="eg. Street 221"
          />
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-12 col-sm-6">
          <label>City</label>
          <soft-input
            id="city"
            class="multisteps-form__input"
            type="text"
            placeholder="eg. Tokyo"
          />
        </div>
        <div class="col-6 col-sm-3 mt-3 mt-sm-0">
          <label>State</label>
          <select
            id="choices-state"
            class="multisteps-form__select form-control"
            name="choices-state"
          >
            <option selected="selected">...</option>
            <option value="1">State 1</option>
            <option value="2">State 2</option>
          </select>
        </div>
        <div class="col-6 col-sm-3 mt-3 mt-sm-0">
          <label>Zip</label>
          <soft-input
            id="zipCode"
            class="multisteps-form__input"
            type="text"
            placeholder="7 letters"
          />
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
          class="ms-auto js-btn-next"
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
import Choices from "choices.js";

export default {
  name: "Address",
  components: {
    SoftInput,
    SoftButton,
  },
  mounted() {
    if (document.getElementById("choices-state")) {
      var element = document.getElementById("choices-state");
      new Choices(element, {
        searchEnabled: false,
      });
    }
  },
};
</script>

<style></style>
