import { useCallback, useEffect, useState } from "react";
import "./App.css";
import { PdfViewer } from "react-pdf-selection";

function App() {
  const [areaSelectionActive, setAreaSelectionActive] = useState(true);
  const [isPopUp, setIsPopUp] = useState(false);
  const [popUpPlacement, setPopUpPlacement] = useState({});
  const [normalizedPlacement, setNormalizedPlacement] = useState({});
  const [selections, setSelections] = useState([]);
  const [tag, setTag] = useState("");

  return (
    <>
      <div className="flex">
        <div
          className={`absolute z-50 bg-black w-[50svw] h-full opacity-80 ${
            isPopUp ? "visible" : "hidden"
          }`}
        >
          <div className="flex justify-end ">
            <button
              className=" h-[2svh] text-blue-600"
              onClick={() => {
                setIsPopUp(false);
              }}
            >
              Close
            </button>
          </div>
          <div className="flex justify-items-center space-x-[2svw] ">
            <div className="text-blue-600">Tag Name</div>
            <input
              value={tag}
              onChange={(e) => {
                setTag(e.target.value);
              }}
            />
          </div>
          <button
            className="text-blue-600 bg-emerald-950 border-2 border-blue-600 rounded-sm w-[5svw] text-center"
            onClick={() => {
              setSelections([
                ...selections,
                { ...normalizedPlacement, tag: tag.trim() },
              ]);
              setIsPopUp(false);
              setTag("");
            }}
          >
            Insert
          </button>
        </div>
        <div className="left-0 top-0 h-[100svh] flex-1 overflow-y-auto relative">
          <PdfViewer
            url={"/INV-7278395(Nov 10).pdf"}
            enableAreaSelection={useCallback(
              () => areaSelectionActive,
              [areaSelectionActive]
            )}
            onAreaSelection={(area) => {
              console.log(area);
              if (!area || area.image.length < 20) return;
              console.log(area.position.absolute.boundingRect);
              setPopUpPlacement(area.position.absolute.boundingRect);
              setNormalizedPlacement(area.position.normalized.boundingRect);
              setIsPopUp(true);
            }}
            // onLoad={(dim) => console.log(dim)}
          />
        </div>

        <div className="flex-1">
          <table>
            <tbody>
              <tr>
                <td>Tag</td>
                <td>bottom</td>
                <td>right</td>
                <td>top</td>
                <td>left</td>
              </tr>
              {selections.map((selection) => {
                console.log(selection);
                return (
                  <tr>
                    <td>{selection.tag}</td>
                    <td>{selection.bottom}</td>
                    <td>{selection.right}</td>
                    <td>{selection.top}</td>
                    <td>{selection.left}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
}

export default App;
