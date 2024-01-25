<!-- Template -->

<template>

<div id="container">

	<div id="login-container">
		<h1>Badger</h1>
		<h2 id="caption">Log in to view your badge.</h2>
		<form>
			<label for="badgeId"><h2>Badge ID</h2></label>
			<div id="flex-container">
				<input type="text" name="badgeId" id="badgeId" />
				<img class="proceed" id="proceed" />
			</div>
		</form>
		<router-link to="/staff-login" id="staff-link">Switch to Staff Login</router-link>
	</div>

	<div id="hint-container">
		<h1>Hint</h1>
		<h2>Your badge ID is an 8 character code found on the back of your badge.</h2>
		<div id="cards">
			<center>
				<img src="@/assets/svg/card_front.svg" />
				<img src="@/assets/svg/card_back.svg" />
			</center>
		</div>
	</div>

</div>

</template>

<!-- Script -->

<script lang="ts">
</script>

<!-- Style -->

<style scoped>

#badgeId {
	background-color: var(--light);
	border-width: 0px;
	border-radius: 10px;
	padding: 2px 0.5em;
	font-size: 20px;
}

#caption {
	margin-top: 84px;
	margin-bottom: 32px;
}

#cards {
	margin-top: 32px;
	width: 100%;
}

#cards center img {
	padding: 16px;
	height: 300px;
}

#proceed {
	margin-left: 16px;
}

#staff-link {
	position: absolute;
	bottom: 8px;
	right: 16px;
	color: var(--medium);
	text-decoration: none;
	font-size: 16px;
}

/* Containers */

#container {
	display: grid;
	grid-template-columns: 50% 50%;
	grid-template-rows: 100% 100%;
	height: 100vh;
	width: 100%;
}

#hint-container {
	background-color: var(--light);
	padding-left: 72px;
	padding-top: 42px;
	padding-right: 32px;
	color: var(--black);
}

#login-container {
	position: relative;
	background-color: var(--dark);
	padding-left: 64px;
	padding-top: 42px;
}

#flex-container {
	display: flex;
    align-items: center;
	margin-top: 8px;
}

</style>
