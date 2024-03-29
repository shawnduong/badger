# Status

## Public

- [ ] POST /public/reset: Request a password reset.
- [ ] Tests

## User

- [x] GET /user/user: Get your own user account details.
- [x] POST /user/user: Create a user account to link your card to.
- [x] PATCH /user/user: Update the information in a user account.
- [x] Tests

- [x] GET /user/announcement: Get all announcements.
- [x] Tests

- [x] POST /user/submission/{code}: Redeem a code for points.
- [x] Tests

- [x] GET /user/event: Get all events.
- [x] Tests

- [x] GET /user/rsvp: Get all your RSVPs.
- [x] POST /user/rsvp/{eventId}: Submit an RSVP for an event.
- [x] DELETE /user/rsvp/{eventId}: Delete an RSVP for an event.
- [x] Tests

- [x] GET /user/attendance: Get all your attendances.
- [x] POST /user/attendance/{code}: Submit an attendance code.
- [x] Tests

- [x] GET /user/entitlement: Get a list of all the entitlements available.
- [x] Tests

- [x] GET /user/redemption: Get a list of all your entitlement redemptions.
- [x] Tests

- [x] GET /user/reward: Get a list of all the rewards available.
- [x] Tests

- [x] GET /user/claim: Get a list of all your reward claims.
- [x] POST /user/claim/{rewardId}: Claim a reward.
- [x] Tests

## Manage

- [x] GET /manage/code: Get a list of all codes and their values.
- [x] POST /manage/code: Create a code.
- [x] GET /manage/code/{codeId}: Get information about one code in particular.
- [x] PATCH /manage/code/{codeId}: Update a code.
- [x] DELETE /manage/code/{codeId}: Delete a code.
- [x] Tests

- [x] GET /manage/submission: Get a list of all submissions.
- [x] POST /manage/submission: Create a submission.
- [x] PATCH /manage/submission/{submissionId}: Update a submission.
- [x] DELETE /manage/submission/{submissionId}: Delete a submission.
- [x] Tests

- [x] POST /manage/announcement: Create an announcement.
- [x] PATCH /manage/announcement/{announcementId}: Update an announcement.
- [x] DELETE /manage/announcement/{announcementId}: Delete an announcement.
- [x] Tests

- [x] POST /manage/event: Create an event.
- [x] PATCH /manage/event/{eventId}: Update an event.
- [x] DELETE /manage/event/{eventId}: Delete an event.
- [x] Tests

- [x] GET /manage/rsvp: Get a list of all RSVPs.
- [x] POST /manage/rsvp: Create an RSVP on a user's behalf.
- [x] PATCH /manage/rsvp/{rsvpId}: Update an RSVP.
- [x] DELETE /manage/rsvp/{rsvpId}: Delete an RSVP.
- [x] Tests

- [x] GET /manage/attendance: Get a list of all attendances.
- [x] POST /manage/attendance: Create an attendance on a user's behalf.
- [x] PATCH /manage/attendance/{attendanceId}: Update an attendance.
- [x] DELETE /manage/attendance/{attendanceId}: Delete an attendance.
- [x] Tests

- [x] POST /manage/entitlement: Create an entitlement.
- [x] PATCH /manage/entitlement/{entitlementId}: Update an entitlement.
- [x] DELETE /manage/entitlement/{entitlementId}: Delete an entitlement.
- [x] Tests

- [x] GET /manage/redemption: Get a list of all redemptions.
- [x] POST /manage/redemption: Create a redemption on behalf of a user.
- [x] PATCH /manage/redemption/{redemptionId}: Update a redemption.
- [x] DELETE /manage/redemption/{redemptionId}: Delete a redemption.
- [x] Tests

- [x] POST /manage/reward: Create a reward.
- [x] PATCH /manage/reward/{rewardId}: Update a reward.
- [x] DELETE /manage/reward/{rewardId}: Delete a reward.
- [x] Tests

- [x] GET /manage/claim: Get a list of all reward claims.
- [x] POST /manage/claim: Create a reward claim on a user's behalf.
- [x] PATCH /manage/claim/{claimId}: Update a reward claim.
- [x] DELETE /manage/claim/{claimId}: Delete a reward claim.
- [x] Tests

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

- [x] GET /admin/configure: Get the scanner configurations.
- [x] POST /admin/configure: Create a scanner configuration.
- [x] PATCH /admin/configure/{configurationId}: Update a configuration.
- [x] DELETE /admin/configure/{configurationId}: Delete a configuration.
- [x] Tests

- [ ] GET /admin/scanner: Get a list of scanner statuses.
- [ ] Tests

## Scanner

- [ ] POST /scanner/scan: Report a batch of scans.
- [ ] Tests

- [ ] POST /scanner/ping: Report that this scanner is still alive.
- [ ] Tests
