import { defineStore } from "pinia";
import User from "./User";

export const useUserStore = defineStore({
  id: "userStore",
  state: () => ({
    loggedIn:
      localStorage["loggedIn"] || localStorage["loggedIn"] === "true"
        ? true
        : false,
    user: null,
  }),
  getters: {
    doubleCount: (state) => state.counter * 2,
  },
  actions: {
    increment() {
      this.counter++;
    },
    setUser(username = "", weight = null, height = null, bodyShape = null) {
      this.loggedIn = true;
      localStorage.setItem("loggedIn", true);
      this.user = new User(username, weight, height, bodyShape);
    },
  },
});
