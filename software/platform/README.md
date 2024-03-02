# Status

## Public

- [ ] POST /public/reset: Request a password reset.
- [ ] Tests

## User

- [x] GET /user/user: Get your own user account details.
- [x] POST /user/user: Create a user account to link your card to.
- [x] PATCH /user/user: Update the information in a user account.
- [x] Tests

- [ ] GET /user/announcement: Get all announcements.
- [ ] Tests

- [ ] POST /user/submission/{code}: Redeem a code for points.
- [ ] Tests

- [ ] GET /user/event: Get all events.
- [ ] Tests

- [ ] GET /user/rsvp: Get all your RSVPs.
- [ ] POST /user/rsvp/{eventId}: Submit an RSVP for an event.
- [ ] DELETE /user/rsvp/{eventId}: Delete an RSVP for an event.
- [ ] Tests

- [ ] GET /user/attendance: Get all your attendances.
- [ ] POST /user/attendance/{code}: Submit an attendance code.
- [ ] Tests

- [ ] GET /user/entitlement: Get a list of all the entitlements available.
- [ ] Tests

- [ ] GET /user/redemption: Get a list of all your entitlement redemptions.
- [ ] Tests

- [ ] GET /user/reward: Get a list of all the rewards available.
- [ ] Tests

- [ ] GET /user/claim: Get a list of all your reward claims.
- [ ] POST /user/claim/{rewardId}: Claim a reward.
- [ ] Tests

## Manage

- [x] GET /manage/code: Get a list of all codes and their values.
- [x] POST /manage/code: Create a code.
- [x] PATCH /manage/code/{codeId}: Update a code.
- [x] DELETE /manage/code/{codeId}: Delete a code.
- [x] Tests

- [ ] GET /manage/submission: Get a list of all submissions.
- [ ] POST /manage/submission: Create a submission.
- [ ] PATCH /manage/submission/{submissionId}: Update a submission.
- [ ] DELETE /manage/submission/{submissionId}: Delete a submission.
- [ ] Tests

- [ ] POST /manage/announcement: Create an announcement.
- [ ] PATCH /manage/announcement/{announcementId}: Update an announcement.
- [ ] DELETE /manage/announcement/{announcementId}: Delete an announcement.
- [ ] Tests

- [ ] POST /manage/event: Create an event.
- [ ] PATCH /manage/event/{eventId}: Update an event.
- [ ] DELETE /manage/event/{eventId}: Delete an event.
- [ ] Tests

- [ ] GET /manage/rsvp: Get a list of all RSVPs.
- [ ] POST /manage/rsvp: Create an RSVP on a user's behalf.
- [ ] PATCH /manage/rsvp/{rsvpId}: Update an RSVP.
- [ ] DELETE /manage/rsvp/{rsvpId}: Delete an RSVP.
- [ ] Tests

- [ ] GET /manage/attendance: Get a list of all attendances.
- [ ] POST /manage/attendance: Create an attendance on a user's behalf.
- [ ] PATCH /manage/attendance/{attendanceId}: Update an attendance.
- [ ] DELETE /manage/attendance/{attendanceId}: Delete an attendance.
- [ ] Tests

- [ ] POST /manage/entitlement: Create an entitlement.
- [ ] PATCH /manage/entitlement/{entitlementId}: Update an entitlement.
- [ ] DELETE /manage/entitlement/{entitlementId}: Delete an entitlement.
- [ ] Tests

- [ ] GET /manage/redemption: Get a list of all redemptions.
- [ ] POST /manage/redemption: Create a redemption on behalf of a user.
- [ ] PATCH /manage/redemption/{redemptionId}: Update a redemption.
- [ ] DELETE /manage/redemption/{redemptionId}: Delete a redemption.
- [ ] Tests

- [ ] POST /manage/reward: Create a reward.
- [ ] PATCH /manage/reward/{rewardId}: Update a reward.
- [ ] DELETE /manage/reward/{rewardId}: Delete a reward.
- [ ] Tests

- [ ] GET /manage/claim: Get a list of all reward claims.
- [ ] POST /manage/claim: Create a reward claim on a user's behalf.
- [ ] PATCH /manage/claim/{claimId}: Update a reward claim.
- [ ] DELETE /manage/claim/{claimId}: Delete a reward claim.
- [ ] Tests

## Admin

- [x] GET /admin/user: Get all users and their account info.
- [x] POST /admin/user: Create a user account.
- [x] GET /admin/user/{userId}: Get information about one account in particular.
- [x] PATCH /admin/user/{userId}: Update the information in a user account.
- [x] DELETE /admin/user/{userId}: Delete an account.
- [x] Tests

- [x] GET /admin/policy: Get the policy settings.
- [x] PATCH /admin/policy: Change the policy settings.
- [x] Tests

- [ ] GET /admin/reset: Get a list of all requested account resets.
- [ ] PATCH /admin/reset/{resetId}: Update an account reset.
- [ ] DELETE /admin/reset/{resetId}: Delete a reset request.
- [ ] Tests

- [ ] GET /admin/configure: Get the scanner configurations.
- [ ] POST /admin/configure: Create a scanner configuration.
- [ ] PATCH /admin/configure/{configurationId}: Update a configuration.
- [ ] DELETE /admin/configure/{configurationId}: Delete a configuration.
- [ ] Tests

- [ ] GET /admin/scanner: Get a list of scanner statuses.
- [ ] Tests

## Scanner

- [ ] POST /scanner/scan: Report a batch of scans.
- [ ] Tests

- [ ] POST /scanner/ping: Report that this scanner is still alive.
- [ ] Tests
