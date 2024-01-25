import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router"
import LoginView from "../views/LoginView.vue"
import StaffLoginView from "../views/StaffLoginView.vue"

const routes: Array<RouteRecordRaw> = [
	{
		path: "/",
		name: "home",
		component: LoginView
	},
	{
		path: "/staff-login",
		name: "staff-login",
		component: StaffLoginView
	}
]

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes
})

export default router
