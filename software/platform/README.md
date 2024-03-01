# Status

## Public

- [ ] POST /public/reset: Request a password reset.
  - [ ] Test

## User

- [x] GET /user/user: Get your own user account details.
  - [x] Test
- [x] POST /user/user: Create a user account to link your card to.
  - [x] Test
- [x] PATCH /user/user: Update the information in a user account.
  - [x] Test

- [ ] GET /user/announcement: Get all announcements.
  - [ ] Test

- [ ] POST /user/code/{code}: Redeem a code for points.
  - [ ] Test

- [ ] GET /user/event: Get all events.
  - [ ] Test

- [ ] GET /user/rsvp: Get all your RSVPs.
  - [ ] Test
- [ ] POST /user/rsvp/{eventId}: Submit an RSVP for an event.
  - [ ] Test
- [ ] DELETE /user/rsvp/{eventId}: Delete an RSVP for an event.
  - [ ] Test

- [ ] GET /user/attendance: Get all your attendances.
  - [ ] Test
- [ ] POST /user/attendance/{code}: Submit an attendance code.
  - [ ] Test

- [ ] GET /user/entitlement: Get a list of all the entitlements available.
  - [ ] Test

- [ ] GET /user/redemption: Get a list of all your entitlement redemptions.
  - [ ] Test

- [ ] GET /user/reward: Get a list of all the rewards available.
  - [ ] Test

- [ ] GET /user/claim: Get a list of all your reward claims.
  - [ ] Test
- [ ] POST /user/claim/{rewardId}: Claim a reward.
  - [ ] Test

## Manage

- [ ] GET /manage/code: Get a list of all codes and their values.
  - [ ] Test
- [ ] POST /manage/code: Create a code.
  - [ ] Test
- [ ] PATCH /manage/code/{codeId}: Update a code.
  - [ ] Test
- [ ] DELETE /manage/code/{codeId}: Delete a code.
  - [ ] Test

- [ ] POST /manage/announcement: Create an announcement.
  - [ ] Test
- [ ] PATCH /manage/announcement/{announcementId}: Update an announcement.
  - [ ] Test
- [ ] DELETE /manage/announcement/{announcementId}: Delete an announcement.
  - [ ] Test

- [ ] POST /manage/event: Create an event.
  - [ ] Test
- [ ] PATCH /manage/event/{eventId}: Update an event.
  - [ ] Test
- [ ] DELETE /manage/event/{eventId}: Delete an event.
  - [ ] Test

- [ ] GET /manage/rsvp: Get a list of all RSVPs.
  - [ ] Test
- [ ] POST /manage/rsvp: Create an RSVP on a user's behalf.
  - [ ] Test
- [ ] PATCH /manage/rsvp/{rsvpId}: Update an RSVP.
  - [ ] Test
- [ ] DELETE /manage/rsvp/{rsvpId}: Delete an RSVP.
  - [ ] Test

- [ ] GET /manage/attendance: Get a list of all attendances.
  - [ ] Test
- [ ] POST /manage/attendance: Create an attendance on a user's behalf.
  - [ ] Test
- [ ] PATCH /manage/attendance/{attendanceId}: Update an attendance.
  - [ ] Test
- [ ] DELETE /manage/attendance/{attendanceId}: Delete an attendance.
  - [ ] Test

- [ ] POST /manage/entitlement: Create an entitlement.
  - [ ] Test
- [ ] PATCH /manage/entitlement/{entitlementId}: Update an entitlement.
  - [ ] Test
- [ ] DELETE /manage/entitlement/{entitlementId}: Delete an entitlement.
  - [ ] Test

- [ ] GET /manage/redemption: Get a list of all redemptions.
  - [ ] Test
- [ ] POST /manage/redemption: Create a redemption on behalf of a user.
  - [ ] Test
- [ ] PATCH /manage/redemption/{redemptionId}: Update a redemption.
  - [ ] Test
- [ ] DELETE /manage/redemption/{redemptionId}: Delete a redemption.
  - [ ] Test

- [ ] POST /manage/reward: Create a reward.
  - [ ] Test
- [ ] PATCH /manage/reward/{rewardId}: Update a reward.
  - [ ] Test
- [ ] DELETE /manage/reward/{rewardId}: Delete a reward.
  - [ ] Test

- [ ] GET /manage/claim: Get a list of all reward claims.
  - [ ] Test
- [ ] POST /manage/claim: Create a reward claim on a user's behalf.
  - [ ] Test
- [ ] PATCH /manage/claim/{claimId}: Update a reward claim.
  - [ ] Test
- [ ] DELETE /manage/claim/{claimId}: Delete a reward claim.
  - [ ] Test

## Admin

- [x] GET /admin/user: Get all users and their account info.
  - [x] Test
- [x] POST /admin/user: Create a user account.
  - [x] Test
- [ ] PATCH /admin/user/{userId}: Update the information in a user account.
  - [ ] Test
- [x] DELETE /admin/user/{userId}: Delete an account.
  - [x] Test

- [ ] GET /admin/policy: Get the policy settings.
  - [ ] Test
- [ ] PATCH /admin/policy: Change the policy settings.
  - [ ] Test

- [ ] GET /admin/reset: Get a list of all requested account resets.
  - [ ] Test
- [ ] PATCH /admin/reset/{resetId}: Update an account reset.
  - [ ] Test
- [ ] DELETE /admin/reset/{resetId}: Delete a reset request.
  - [ ] Test

- [ ] GET /admin/configure: Get the scanner configurations.
  - [ ] Test
- [ ] POST /admin/configure: Create a scanner configuration.
  - [ ] Test
- [ ] PATCH /admin/configure/{configurationId}: Update a configuration.
  - [ ] Test
- [ ] DELETE /admin/configure/{configurationId}: Delete a configuration.
  - [ ] Test

- [ ] GET /admin/scanner: Get a list of scanner statuses.
  - [ ] Test

## Scanner

- [ ] POST /scanner/scan: Report a batch of scans.
  - [ ] Test

- [ ] POST /scanner/ping: Report that this scanner is still alive.
  - [ ] Test
