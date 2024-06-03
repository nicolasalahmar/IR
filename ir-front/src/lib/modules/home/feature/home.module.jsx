//@Third Party
import ReactSelect from "react-select";
import { useSelector, useDispatch } from "react-redux";
import { createSearchParams, useNavigate } from "react-router-dom";

//@Dev
// # Shared
// ## Utils
import { DATA_SETS } from "@/shared/utils";
// ## UI
import { NormalButtonInput } from "@/shared/ui";
// # Locale
// ## Store
import { selectSelectedDataSet, setSelectedDataSetRed } from "../data-access";

export function HomeModule() {
  //* @Initiate
  const nav = useNavigate();
  const dispatch = useDispatch();

  //* @Component State
  const selectedDataSet = useSelector(selectSelectedDataSet);

  //* @Handlers
  const setSelectedDataSet = (value) =>
    dispatch(setSelectedDataSetRed({ selectedDataSet: value }));

  const handleButtonClick = () =>
    nav({
      pathname: "search-engine",
      search: createSearchParams({
        dataset: selectedDataSet?.label?.toLowerCase(),
      }).toString(),
    });

  return (
    <div className="w-screen h-screen flex-center bg-darkGray-light flex-col gap-6">
      <ReactSelect
        value={selectedDataSet}
        onChange={setSelectedDataSet}
        options={DATA_SETS}
        className="w-96"
      />
      <NormalButtonInput
        className="w-48 h-11"
        label={"Done"}
        onClick={handleButtonClick}
        disabled={!selectedDataSet}
      />
    </div>
  );
}
