export default function WellSelector() {
  return (
    <section className="panel">
      <h2>Well</h2>
      <label>
        Select a well
        <select defaultValue="">
          <option value="" disabled>
            No wells yet
          </option>
        </select>
      </label>
      <label className="file-field">
        FMI image
        <input type="file" />
      </label>
      <label className="file-field">
        Well logs
        <input type="file" />
      </label>
    </section>
  );
}
