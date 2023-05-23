<template>
  <div>
    <div class="form-group" v-if="genres">
      <form @submit.prevent="signUp" class="signup-form">
        <div>
          <label for="username" class="title-tag">* Username</label>
          <input
            type="text"
            v-model="username"
            id="username"
            required
            placeholder="Enter your name"
            min="3"
            max="50"
          />
        </div>
        <!-- <p class="error-message">
          으아악, 이름을 입력하세요
        </p>
        <p class="success-message">
          으아악, 이름을 입력하기성공
        </p> -->
        <div>
          <label for="email" class="title-tag">* Email</label>
          <input
            type="email"
            v-model="email"
            id="email"
            autocomplete="off"
            required
            placeholder="Enter your email"
          />
        </div>
        <div>
          <label for="password" class="title-tag">* Password</label>
          <input
            type="password"
            v-model="password"
            id="password"
            required
            placeholder="Enter your password"
          />
        </div>
        <div>
          <label for="passwordConfirm" class="title-tag"
            >* Check password</label
          >
          <input
            type="password"
            v-model="passwordConfirm"
            id="passwordConfirm"
            required
            placeholder="Check your password"
          />
        </div>
        <div class="card-container">
          <p class="title-tag">* 선호하는 장르</p>
          <section class="genre-card">
            <div v-for="genre in genres" :key="genre.id" class="genre">
              <span
                :value="genre.id"
                @click="saveGenre(genre.id)"
                :class="{ selected: isSelected(genre.id) }"
                class="genre-btn"
                >{{ genre.name }}</span
              >
            </div>
          </section>
          <section clas="goal-card">
            <label for="goal_of_month" class="title-tag"
              >* 이번 달에는<br />
              <b-form-select
                v-model="goal_of_month"
                :options="options"
                id="goal-select"
              ></b-form-select>
              <br />개의 영화를 보고싶어요.
            </label>
          </section>
        </div>
        <input type="submit" value="Sign Up >" class="signup-btn" />
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "SignupForm",
  data() {
    return {
      username: null,
      email: null,
      password: null,
      passwordConfirm: null,
      goal_of_month: 1,
      favorite_genre: [],
      options: [
        { value: 1, text: "1" },
        { value: 2, text: "2" },
        { value: 3, text: "3" },
        { value: 4, text: "4" },
        { value: 5, text: "5" },
        { value: 6, text: "6" },
        { value: 7, text: "7" },
        { value: 8, text: "8" },
        { value: 9, text: "9" },
        { value: 10, text: "10" },
      ],
    };
  },
  created() {
    this.fetchGenres();
  },
  computed: {
    genres() {
      return this.$store.state.genres;
    },
  },
  methods: {
    signUp() {
      const username = this.username;
      const email = this.email;
      const password = this.password;
      const passwordConfirm = this.passwordConfirm;
      const goal_of_month = this.goal_of_month;
      const favorite_genre = this.favorite_genre;

      const payload = {
        username,
        password,
        passwordConfirm,
        email,
        goal_of_month,
        favorite_genre,
      };
      this.$store.dispatch("signUp", payload);
    },

    fetchGenres() {
      this.$store.dispatch("fetchGenres");
    },

    saveGenre(genre_id) {
      const index = this.favorite_genre.indexOf(genre_id);
      if (index === -1) {
        console.log(this.favorite_genre);
        this.favorite_genre.push(genre_id);
        if (this.favorite_genre.length > 5) {
          alert("장르는 5개까지만 선택할 수 있습니다!");
          this.favorite_genre.splice(index, 1);
        }
      } else {
        this.favorite_genre.splice(index, 1);
      }
    },

    isSelected(genre_id) {
      return this.favorite_genre.includes(genre_id);
    },
  },
};
</script>

<style scoped>
* {
  background: #f4f3ee;
}
.form-group {
  margin: 5em;
}
.signup-form {
  display: flex;
  flex-direction: column;
}
.title-tag {
  font-size: 1.7em;
  font-weight: 700;
  color: #3b322c;
}
.genre-card {
  display: flex;
  flex-wrap: wrap;
  gap: 20px 2%;
  width: 50%;
  margin-bottom: 2em;
}

.genre-btn {
  background-color: #8ddca4;
  color: #3b322c;
  display: inline-block;
  border: solid 1px white;
  border-radius: 20px;
  padding: 10px 20px;
  cursor: pointer;
}

.selected {
  background-color: #f58080;
  color: #f4f3ee;
}
.genre-btn:hover {
  background-color: #3b322c;
  color: #f4f3ee;
  transition: 0.1s;
}

#goal-select {
  outline: none;
  font-size: 3em;
  color: #f58080;
}
#goal-select:hover {
  color: #8ddca4;
  cursor: pointer;
}

.signup-btn {
  display: block;
  font-size: 4em;
  font-weight: 600;
  color: #3b322c;
  align-self: flex-end;
  background: linear-gradient(to right, #f58080, #8ddca4);
  animation: rainbow 2s ease-in-out infinite;
  background-clip: text;
  -webkit-background-clip: text;
  transition: color 0.2s ease-in-out;
}
.signup-btn:hover {
  color: rgba(0, 0, 0, 0);
}
@keyframes rainbow {
  0% {
    background-position: left;
  }
  50% {
    background-position: right;
  }
  100% {
    background-position: left;
  }
}

input[type="text"],
input[type="password"],
input[type="email"] {
  width: 100%;
  height: 50px;
  font-size: 1.5em;
  outline: none;
  padding-left: 20px;
  color: #627278;
  border-bottom: 1px solid #627278;
  transition: border-width 0.6s linear;
  margin-bottom: 20px;
}

input[type="text"]:focus,
input[type="password"]:focus,
input[type="email"]:focus {
  animation-name: border-focus;
  animation-duration: 0.5s;
  animation-fill-mode: forwards;
}
@keyframes border-focus {
  from {
    border-bottom: 1px solid #627278;
  }
  to {
    border-bottom: 3px solid #f58080;
  }
}

.error-message{
  display: none;
  margin-left: 1.3em;
  margin-bottom: 2em;
  color: #f58080;
  font-weight: 600;
}
.success-message{
  display: none;
  margin-left: 1.3em;
  margin-bottom: 2em;
  color: #8ddca4;
  font-weight: 600;
}

input:valid + .success-message{
  display: show;
}
</style>