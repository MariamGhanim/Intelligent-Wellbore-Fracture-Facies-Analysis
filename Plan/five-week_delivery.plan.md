<style>
@page { margin: 14mm 14mm; }
html, body, .markdown-body, .markdown-preview, .markdown-preview-section {
  font-family: "Segoe UI", Calibri, sans-serif !important;
  font-size: 14px !important;
  line-height: 1.45 !important;
  color: #243140 !important;
}
h1 {
  font-family: Georgia, "Times New Roman", serif !important;
  font-size: 24px !important;
  color: #16324F !important;
  margin: 0 0 8px !important;
  padding-bottom: 6px !important;
  border-bottom: 2px solid #16324F !important;
  line-height: 1.2 !important;
}
h2 {
  font-size: 17px !important;
  color: #16324F !important;
  background: #F3F6F8 !important;
  border-left: 4px solid #1F6F8B !important;
  padding: 6px 10px !important;
  margin: 16px 0 8px !important;
  line-height: 1.25 !important;
}
h3 {
  font-size: 15px !important;
  color: #0E6B4F !important;
  margin: 12px 0 4px !important;
  line-height: 1.25 !important;
}
p, li { font-size: 14px !important; margin-top: 4px !important; margin-bottom: 4px !important; }
ul, ol { margin: 4px 0 8px !important; padding-left: 22px !important; }
li { margin: 2px 0 !important; }
hr { border: none !important; border-top: 1px solid #E3E8EC !important; margin: 12px 0 !important; }
blockquote {
  margin: 8px 0 12px !important;
  padding: 8px 12px !important;
  background: #F8F4EA !important;
  border-left: 4px solid #8A6A2F !important;
  color: #3E4A54 !important;
  font-size: 14px !important;
}
strong { color: #16324F; }
</style>

# Intelligent Wellbore Fracture & Facies Analysis

<div style="font-family: Segoe UI, Calibri, sans-serif; font-size: 13px; color: #5C6B76; margin: 4px 0 12px;">Delivery plan · app 27 September – 15 December 2026 · Ahmed’s documentation and Mariam’s slides before 20 January 2027</div>


## The project

The project is an AI-based software system for the automated interpretation of wellbore image logs and conventional well logs.

The main goal is to analyze FMI (Formation MicroImager) wellbore images together with well-log data to automatically detect geological fractures, determine their depth and orientation, visualize them using tadpole plots, and classify subsurface intervals into different facies/zones.

A user creates an account, uploads data for a well, and clicks **Analyze Well**. The system then automatically processes the well through the complete analysis pipeline: fracture detection, fracture geometry, tadpole visualization, well-log integration, and facies/zone classification. The results are stored under the user's account and can be viewed later through the dashboard, along with a generated well analysis report.

**Mariam** owns the screens, the AI models, the assistant, and the calculations: depth, dip, azimuth, and log alignment. **Ahmed** owns the backend only: accounts, the database, file storage, and the APIs.

<div style="font-family: Segoe UI, Calibri, sans-serif; background: #F7F5F1; border: 1px solid #E4DDD2; border-radius: 10px; padding: 14px 16px 12px; margin: 10px 0 6px;">
  <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 18px; color: #16324F;">Project pipeline</div>
  <div style="color: #6A7782; font-size: 13px; margin: 2px 0 10px;">Each step feeds the next · 27 Sep – 15 Dec 2026</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 12px; font-size: 13px; color: #243140;">
    <div style="background: #fff; border-radius: 6px; padding: 7px 10px;"><span style="color: #1F6F8B; font-weight: 700;">01</span> &nbsp; Sign up / Log in / Reset password</div>
    <div style="background: #fff; border-radius: 6px; padding: 7px 10px;"><span style="color: #1F6F8B; font-weight: 700;">07</span> &nbsp; Facies / Zone Classification</div>
    <div style="background: #fff; border-radius: 6px; padding: 7px 10px;"><span style="color: #1F6F8B; font-weight: 700;">02</span> &nbsp; FMI Image</div>
    <div style="background: #fff; border-radius: 6px; padding: 7px 10px;"><span style="color: #1F6F8B; font-weight: 700;">08</span> &nbsp; Database</div>
    <div style="background: #fff; border-radius: 6px; padding: 7px 10px;"><span style="color: #1F6F8B; font-weight: 700;">03</span> &nbsp; Fracture Detection</div>
    <div style="background: #fff; border-radius: 6px; padding: 7px 10px;"><span style="color: #1F6F8B; font-weight: 700;">09</span> &nbsp; AI Agent</div>
    <div style="background: #fff; border-radius: 6px; padding: 7px 10px;"><span style="color: #1F6F8B; font-weight: 700;">04</span> &nbsp; Fracture Geometry</div>
    <div style="background: #fff; border-radius: 6px; padding: 7px 10px;"><span style="color: #1F6F8B; font-weight: 700;">10</span> &nbsp; Interactive Dashboard</div>
    <div style="background: #fff; border-radius: 6px; padding: 7px 10px;"><span style="color: #1F6F8B; font-weight: 700;">05</span> &nbsp; Tadpole Visualization</div>
    <div style="background: #fff; border-radius: 6px; padding: 7px 10px;"><span style="color: #1F6F8B; font-weight: 700;">11</span> &nbsp; My Reports — this user only</div>
    <div style="background: #fff; border-radius: 6px; padding: 7px 10px;"><span style="color: #1F6F8B; font-weight: 700;">06</span> &nbsp; Well-Log Integration</div>
    <div style="background: #16324F; color: #fff; border-radius: 6px; padding: 7px 10px;"><span style="font-weight: 700;">12</span> &nbsp; Download report</div>
  </div>
</div>


---

## Week 1 — Dataset inspection

**27 Sep – 3 Oct**

### Mariam

- List every file for 16A, 16B, and 56-32: FMI format, size, depth range, resolution.
- Decide whether fracture labels are pixel masks, polylines, or a depth / dip / azimuth table.
- Decide whether facies labels exist. Write yes or no and the real class names. Do not invent classes.
- Write how depth is stored, how images align to logs, and the train / test well split.
- Place raw files under `data/raw/`.

### Ahmed

- Confirm the FastAPI app, SQLite, and module folders run locally.
- Add the health check.

> **Checkpoint · 3 Oct** — The data note is written and the API answers `/health`.

---

## Week 2 — Accounts

**4 Oct – 10 Oct**

### Mariam

- Sign up, log in, and log out screens.
- **Forgot password:** enter the account email and set a new password.

### Ahmed

- User table: name, email, password hash.
- Endpoints: sign up, log in, log out, current user, reset password.

> **Checkpoint · 10 Oct** — A new account can sign up, reset its password, and log in again.

---

## Week 3 — Dashboard shell

**11 Oct – 17 Oct**

### Mariam

- After login, show the dashboard: well selector, status, FMI panel, fractures, facies, tadpole, logs, and chat.
- A logged-out visit goes to log in.

### Ahmed

- Agree the JSON for user, well, fracture, status, and report on **11 Oct**.
- Leave the later endpoints in place: upload, analysis, fractures, facies, logs, chat, reports.

> **Checkpoint · 17 Oct** — The dashboard opens only after login.

---

## Week 4 — Read the FMI image

**18 Oct – 24 Oct**

### Mariam

- Read the FMI image the way the data note describes.
- Normalize, handle gaps, and tile large images.
- Map an image row to measured depth from the file metadata.

### Ahmed

- Store the FMI file and serve it through the API.
- Save the depth metadata with the well. He does not calculate depth.

> **Checkpoint · 24 Oct** — One image can be read and a row can be turned into depth.

---

## Week 5 — Show the FMI image

**25 Oct – 31 Oct**

### Mariam

- Upload the FMI file and select the well.
- FMI viewer with a depth scale.

### Ahmed

- Store the upload on the logged-in user.
- Image endpoint ready by **29 Oct**. Another user’s well is not returned.

> **Checkpoint · 31 Oct** — One real well opens with the FMI image and a depth scale.

---

## Week 6 — Well logs

**1 Nov – 7 Nov**

### Mariam

- Align the logs to the FMI depth range. Missing logs stay missing.
- Well-log tracks versus depth.

### Ahmed

- Read the log file and store only the columns that exist.
- Logs API returns those stored curves for the logged-in user.

> **Checkpoint · 7 Nov** — Image and logs share one depth axis.

---

## Week 7 — Prepare fracture training

**8 Nov – 14 Nov**

### Mariam

- Save training samples from the tiled images.
- Choose the model from the real labels. Prefer U-Net if pixel or trace labels exist. If labels are only a table, plan a depth-window detector.
- Write the inference function: image tile in, fracture trace or mask out. Ahmed will call it. He will not change the model.

### Ahmed

- Analysis status: idle, running, done, or failed.

> **Checkpoint · 14 Nov** — Training samples are saved and the status API works.

---

## Week 8 — Train the fracture model

**15 Nov – 21 Nov**

### Mariam

- Train the model. The test well is held out.
- Metrics: precision, recall, F1, and IoU where masks exist.
- Export weights to `models/fracture_model/` with a short model card.
- Do not add a fracture-type head unless type labels are real.

### Ahmed

- The analysis job calls Mariam’s saved model and stores the traces it returns.

> **Checkpoint · 21 Nov** — The model runs on one well and returns traces.

---

## Week 9 — Depth, dip, and azimuth

**22 Nov – 28 Nov**

### Mariam

- Calculate measured depth, dip, and azimuth from each trace.
- Use TVD only if the file has it. Use type only if it is labeled.
- Draw the traces on the FMI image.
- Table: count, depth, dip, azimuth, type, confidence.
- **Analyze Well** starts the job and refreshes when status is done.

### Ahmed

- Save the depth, dip, azimuth, confidence, and optional TVD and type that Mariam calculates.
- Fractures API filters by depth. Each row belongs to the user who ran the analysis.

> **Checkpoint · 28 Nov** — The table matches the database.

---

## Week 10 — Tadpole plot

**29 Nov – 5 Dec**

### Mariam

- Tadpole plot: zoom, filter by depth, filter by type, click a tadpole for that fracture.

### Ahmed

- Tadpole payload: depth, dip, azimuth, id, type.

> **Checkpoint · 5 Dec** — A clicked tadpole matches the same fracture in the table.

---

## Week 11 — Facies

**6 Dec – 12 Dec**

### Mariam

- Features: fracture density, orientation stats, simple image texture, and the available logs.
- If zone labels exist, train one classifier and report accuracy, precision, recall, F1, and a confusion matrix.
- If they do not, show “facies unavailable.” No invented class names.
- Draw the zones beside the logs.

### Ahmed

- Save the facies rows Mariam returns and serve them: start depth, end depth, class, confidence, or an explicit unavailable flag.
- The analysis job calls Mariam’s functions, then saves the rows. Ahmed does not calculate dip, azimuth, or facies.

> **Checkpoint · 12 Dec** — Image, table, tadpole, logs, and zones are on screen.

---

## Week 12 — Assistant, report, and demo

**13 Dec – 15 Dec**

### Ahmed

- Chat endpoint and report download, both limited to the logged-in user.
- Another user’s report is not found. Ahmed does not write the assistant’s answers.

### Mariam

- The assistant answers only from stored rows. A missing field is unavailable.
- Chat on the selected well.
- **My Reports** lists only this account, and each report has **Download**.
- Run the demo once on the held-out well.

> **Checkpoint · 15 Dec** — Two accounts. Each sees and downloads only their own report. The demo script passes.

---

## Demo script

Rehearse this on the held-out well the night before. Use one of 16A(78)-32, 16B(78)-32, or 56-32 — the well that was not used to train the fracture model. Write the real depth window, fracture count, and one fracture id on a card. Every number said out loud must match the screen. If a value was not computed, the assistant says it is unavailable.

**1. Open the problem**

Say what the system is: an interpretation workflow for FMI images and conventional logs. It detects fractures, finds depth, dip, and azimuth, draws a tadpole, and classifies facies where labels exist. Then say the demo is one unseen well, not a slide of training accuracy.

**2. Account**

Create an account on a clean database. Log out. Use **Forgot password**, set a new password, and log in with that password. The dashboard is closed until login succeeds.

**3. Load the well**

Select or upload that well’s FMI image and the log file. Point to the depth range on the FMI viewer before analysis, so the committee sees the raw image first. Name the log curves that actually loaded. Do not claim a curve that is missing.

**4. Analyze Well**

Click **Analyze Well**. While the status runs, walk the pipeline in order: fracture detection, geometry, tadpole, well-log alignment, facies, then save. When status is done, do not describe results that are not on the screen yet.

**5. Fractures on the image**

Show the FMI image with traces drawn on it. Scroll to one clear fracture. Read its measured depth from the table, then show that the same trace sits at that depth on the image. Read dip, azimuth, and confidence from the row. If type or TVD is empty, say the file did not provide it.

**6. Tadpole**

Open the tadpole plot on the same depth range. Zoom in. Filter to dip greater than 60 degrees and show that the table and the plot change together. Click one tadpole and show that its depth, dip, and azimuth are the same fracture as in the table.

**7. Logs and zones**

Show the well logs against the same depth axis as the fractures. If facies intervals exist, point to one interval and its confidence. If they do not, leave the empty state on screen and say zone labels were not in the dataset.

**8. Assistant, from the stored well**

Ask these in the chat, one at a time, and check each answer against the table before moving on:

- How many fractures were detected on this well?
- How many fractures are between the two depths written on the card?
- Which fractures have dip greater than 60 degrees?
- Which depth interval has the highest fracture density?
- Explain fracture number N: depth, dip, azimuth, type if stored, and confidence.
- What is the true vertical depth of that fracture?

The last answer is “unavailable” unless TVD was stored. The count and the dip list must equal the filtered table, not a rounded guess.

**9. Report**

Ask the assistant to generate the report. Open **My Reports**. Open that report in the app and show the same fracture count, orientation summary, and facies result as the dashboard. Download the PDF and show those same figures on the first pages.

**10. The report belongs to this account**

Log out. Log in as a second account. **My Reports** does not list the first report, and that report cannot be opened or downloaded. Log back into the first account and show the report is still there.

---

## Ahmed — Documentation

**16 Dec 2026 – 19 Jan 2027**

Ahmed writes the documentation after the 15 December demo. He must finish it before **20 January 2027**.

---

## Mariam — Presentation slides

**16 Dec 2026 – 19 Jan 2027**

Mariam prepares the presentation slides after the 15 December demo. She must finish them before **20 January 2027**.
